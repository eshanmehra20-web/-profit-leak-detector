const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const html = fs.readFileSync('static/index.html', 'utf8');
const start = html.indexOf('<script>');
const end = html.indexOf('</script>', start + 8);
assert.notEqual(start, -1, 'app script must exist');
assert.notEqual(end, -1, 'app script must close');
assert.equal(html.indexOf('<script>', start + 8), -1, 'app must contain exactly one inline script');
const appScript = html.slice(start + 8, end);

const elements = new Map();
function getElementById(id) {
  if (!elements.has(id)) {
    elements.set(id, {
      id, innerHTML: '', values: {}, handlers: {},
      addEventListener(name, fn) { this.handlers[name] = fn; },
      reset() { this.values = {}; this.wasReset = true; },
    });
  }
  return elements.get(id);
}
const storage = new Map();
const alerts = [];
class FakeFormData {
  constructor(form) { this.values = form.values || {}; }
  get(name) { return this.values[name] ?? ''; }
}
const context = {
  localStorage: {
    getItem(key) { return storage.has(key) ? storage.get(key) : null; },
    setItem(key, value) { storage.set(key, value); },
  },
  document: { getElementById, createElement() { return { click() {} }; } },
  FormData: FakeFormData,
  Blob: class Blob {},
  URL: { createObjectURL() { return 'blob:test'; }, revokeObjectURL() {} },
  alert(message) { alerts.push(message); },
  confirm() { return false; },
};
vm.createContext(context);
vm.runInContext(appScript, context, { timeout: 1000 });

function submit(id, values) {
  const form = getElementById(id);
  form.values = values;
  form.handlers.submit({ preventDefault() {}, target: form });
}

submit('saleForm', { product: 'Pen', quantity: '10', price: '10', cost: '4' });
submit('expenseForm', { name: 'Rent', amount: '120' });
const metrics = getElementById('metrics').innerHTML;
assert.match(metrics, /₹100/);
assert.match(metrics, /₹60/);
assert.match(metrics, /₹200/);
assert.match(metrics, /₹100/);
assert.match(getElementById('products').innerHTML, /Pen/);

const beforeInvalidInput = storage.get('pld.v03');
submit('saleForm', { product: '   ', quantity: '1', price: '10', cost: '5' });
assert.equal(storage.get('pld.v03'), beforeInvalidInput, 'blank product must not overwrite stored data');
assert.ok(alerts.length > 0, 'invalid form should explain the error');

const restore = getElementById('restore');
async function run() {\nawait restore.onchange({ target: {
  files: [{ text: async () => JSON.stringify({ sales: [{ product: 'Bad', q: -1, price: 5, cost: 2 }], expenses: [] }) }],
  value: 'bad.json',
} });
assert.equal(storage.get('pld.v03'), beforeInvalidInput, 'invalid backup must preserve existing data');

await restore.onchange({ target: {
  files: [{ text: async () => JSON.stringify({ sales: [{ product: '<img src=x>', q: 2, price: 20, cost: 10 }], expenses: [] }) }],
  value: 'good.json',
} });
assert.match(getElementById('products').innerHTML, /&lt;img/);
assert.doesNotMatch(getElementById('products').innerHTML, /<img/);
assert.match(getElementById('metrics').innerHTML, /₹40/);

process.stdout.write('Frontend logic tests passed: break-even display, valid form flow, blank-name rejection, invalid-backup preservation, valid restore, and HTML escaping.\n');
}
run().catch(error => { console.error(error); process.exitCode = 1; });
