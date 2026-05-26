// ── Navigation ──────────────────────────────────────────────
function showPage(id) {
  window.location.href = '/' + (id === 'home' ? '' : id);
}

// ── Events tabs ─────────────────────────────────────────────
function switchTab(tab) {
  document.querySelectorAll('.ev-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.events-section').forEach(s => s.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById('tab-' + tab).classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ── Donate amount selector ───────────────────────────────────
var currentAmt = '50';

function selectAmt(el, val) {
  document.querySelectorAll('.amt-btn').forEach(b => b.classList.remove('selected'));
  el.classList.add('selected');
  var customRow = document.getElementById('custom-amount-row');
  if (val === 'custom') {
    if (customRow) customRow.style.display = 'block';
    currentAmt = '';
    var inp = document.getElementById('donate-amount-input');
    if (inp) inp.focus();
    var disp = document.getElementById('donate-display-amt');
    if (disp) disp.textContent = '$__';
  } else {
    if (customRow) customRow.style.display = 'none';
    currentAmt = val;
    var disp = document.getElementById('donate-display-amt');
    if (disp) disp.textContent = '$' + val;
    var pa = document.getElementById('paypal-amount');
    if (pa) pa.value = val;
  }
}

function syncPayPalAmount() {
  var amt = currentAmt;
  if (!amt || amt === 'custom') {
    var custom = document.getElementById('donate-amount-input');
    amt = custom ? custom.value : '';
  }
  if (amt && parseFloat(amt) > 0) {
    var pa = document.getElementById('paypal-amount');
    if (pa) pa.value = amt;
  }
}

document.addEventListener('DOMContentLoaded', function () {
  var inp = document.getElementById('donate-amount-input');
  if (inp) {
    inp.addEventListener('input', function () {
      var v = this.value;
      if (v) {
        currentAmt = v;
        var disp = document.getElementById('donate-display-amt');
        if (disp) disp.textContent = '$' + v;
        var pa = document.getElementById('paypal-amount');
        if (pa) pa.value = v;
      }
    });
  }
});

// ── Card formatting ──────────────────────────────────────────
function formatCard(input) {
  var v = input.value.replace(/\D/g, '').substring(0, 16);
  input.value = v.replace(/(.{4})/g, '$1 ').trim();
}

function formatExpiry(input) {
  var v = input.value.replace(/\D/g, '').substring(0, 4);
  if (v.length >= 2) v = v.substring(0, 2) + ' / ' + v.substring(2);
  input.value = v;
}

function handleCardDonate() {
  var name = document.getElementById('card-name');
  var email = document.getElementById('card-email');
  var cardNum = document.getElementById('card-number');
  var amt = currentAmt;
  if (!amt || amt === 'custom') {
    var ci = document.getElementById('donate-amount-input');
    amt = ci ? ci.value : '';
  }
  if (!name.value.trim() || !email.value.trim() || !cardNum.value.trim() || !amt) {
    alert('Please fill in your name, email, card number, and select an amount.');
    return;
  }
  alert('Thank you, ' + name.value.trim() + '! Your donation of $' + amt + ' is being processed.\n\nA receipt will be sent to ' + email.value.trim() + '.\n\n(Connect to Stripe or PayPal to go live.)');
}
// Events page — show/hide detail panel
function showEventDetail(id) {
  document.querySelectorAll('[id^="detail-"]').forEach(el => el.style.display = 'none');
  document.querySelectorAll('[id^="evt-"]').forEach(el => {
    el.style.background = '';
    el.style.borderLeft = '4px solid transparent';
  });
  document.getElementById('detail-' + id).style.display = 'block';
  document.getElementById('evt-' + id).style.background = 'var(--cream-dark)';
  document.getElementById('evt-' + id).style.borderLeft = '4px solid var(--gold)';
}