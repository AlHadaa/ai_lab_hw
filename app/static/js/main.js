/**
 * Frontend logic for SmartText AI & Vibe Studio
 */

// Preset samples
const SAMPLES = {
  pos: `Artificial intelligence is transforming modern software engineering in remarkable ways. 
The integration of clean code principles, automated testing, and agile prototyping empowers developers to build outstanding, reliable, and high-performance applications with immense confidence and joy!`,
  neg: `The system experienced a critical bug during the release test. 
The server was horribly slow, multiple services failed to respond, and the unexpected crash resulted in a painful loss of data. We must fix this severe problem immediately.`,
  ar: `يعد الذكاء الاصطناعي أداة رائعة ومفيدة جداً للمطورين. 
البرمجة النظيفة تساهم في بناء تطبيقات قوية ومبتكرة وسريعة، والعمل الجماعي يحقق نجاحاً باهراً في مختلف المشاريع التقنية.`
};

// Switch active tab
function switchTab(tabName) {
  const tabs = ['analyzer', 'prompt', 'course'];
  tabs.forEach(t => {
    const el = document.getElementById(`tab-${t}`);
    const btn = document.getElementById(`tab-btn-${t}`);
    if (t === tabName) {
      el.classList.remove('hidden');
      el.classList.add('block');
      btn.classList.add('active');
      btn.classList.remove('text-gray-400');
      btn.classList.add('text-teal-300');
    } else {
      el.classList.add('hidden');
      el.classList.remove('block');
      btn.classList.remove('active');
      btn.classList.add('text-gray-400');
      btn.classList.remove('text-teal-300');
    }
  });
  if (window.lucide) {
    lucide.createIcons();
  }
}

// Load preset sample
function loadSample(type) {
  const textarea = document.getElementById('input-text');
  if (SAMPLES[type]) {
    textarea.value = SAMPLES[type];
    performAnalysis();
  }
}

// Clear text
function clearText() {
  document.getElementById('input-text').value = '';
  resetMetrics();
}

function resetMetrics() {
  document.getElementById('stat-words').innerText = '0';
  document.getElementById('stat-chars').innerText = '0';
  document.getElementById('stat-sentences').innerText = '0';
  document.getElementById('stat-readtime').innerText = '0m';
  document.getElementById('stat-ease').innerText = '--';
  document.getElementById('sentiment-score').innerText = '0.00';
  document.getElementById('sentiment-emoji').innerText = '😐';
  document.getElementById('sentiment-badge').innerText = 'Awaiting input';
  document.getElementById('sentiment-badge').className = 'px-3 py-1 rounded-full text-xs font-semibold bg-gray-800 text-gray-300 border border-gray-700';
  document.getElementById('sentiment-bar').style.width = '50%';
  document.getElementById('sentiment-bar').className = 'h-full rounded-full bg-teal-500 transition-all duration-500';
  document.getElementById('summary-text').innerText = 'Summary will appear here after clicking "Analyze Now".';
  document.getElementById('keywords-container').innerHTML = '<span class="text-xs text-gray-500 italic">No keywords extracted yet</span>';
  document.getElementById('pos-keywords-list').innerHTML = '<span class="text-gray-500 italic">None</span>';
  document.getElementById('neg-keywords-list').innerHTML = '<span class="text-gray-500 italic">None</span>';
}

// Call text analysis API
async function performAnalysis() {
  const text = document.getElementById('input-text').value;
  const btn = document.getElementById('btn-analyze');
  const btnText = document.getElementById('btn-analyze-text');

  btn.disabled = true;
  btnText.innerText = 'Analyzing...';

  try {
    const response = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });

    const result = await response.json();
    if (result.success) {
      renderAnalysis(result.data);
    } else {
      alert('Analysis failed: ' + (result.error || 'Unknown error'));
    }
  } catch (err) {
    console.error('Error analyzing text:', err);
    alert('Network error connecting to API server.');
  } finally {
    btn.disabled = false;
    btnText.innerText = 'Analyze Now';
  }
}

// Render analysis result
function renderAnalysis(data) {
  document.getElementById('stat-words').innerText = data.word_count;
  document.getElementById('stat-chars').innerText = data.char_count;
  document.getElementById('stat-sentences').innerText = data.sentence_count;
  document.getElementById('stat-readtime').innerText = `${Math.ceil(data.readability.reading_time_minutes * 60)}s`;
  document.getElementById('stat-ease').innerText = `${data.readability.reading_ease_score}`;

  // Sentiment
  const s = data.sentiment;
  document.getElementById('sentiment-score').innerText = (s.score > 0 ? '+' : '') + s.score.toFixed(2);
  document.getElementById('sentiment-emoji').innerText = s.emoji;
  
  // Meter: score from -1.0 to +1.0 mapped to 0% - 100%
  const percentage = Math.min(100, Math.max(0, ((s.score + 1) / 2) * 100));
  const bar = document.getElementById('sentiment-bar');
  bar.style.width = `${percentage}%`;

  const badge = document.getElementById('sentiment-badge');
  badge.innerText = s.label;

  if (s.label === 'Positive') {
    badge.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30';
    bar.className = 'h-full rounded-full bg-emerald-500 transition-all duration-500';
  } else if (s.label === 'Negative') {
    badge.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/30';
    bar.className = 'h-full rounded-full bg-rose-500 transition-all duration-500';
  } else {
    badge.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30';
    bar.className = 'h-full rounded-full bg-cyan-500 transition-all duration-500';
  }

  // Keywords lists
  const posContainer = document.getElementById('pos-keywords-list');
  if (s.positive_words && s.positive_words.length > 0) {
    posContainer.innerHTML = s.positive_words.map(w => 
      `<span class="px-2 py-0.5 rounded-md bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">${w}</span>`
    ).join(' ');
  } else {
    posContainer.innerHTML = '<span class="text-gray-500 italic">None</span>';
  }

  const negContainer = document.getElementById('neg-keywords-list');
  if (s.negative_words && s.negative_words.length > 0) {
    negContainer.innerHTML = s.negative_words.map(w => 
      `<span class="px-2 py-0.5 rounded-md bg-rose-500/10 text-rose-300 border border-rose-500/20">${w}</span>`
    ).join(' ');
  } else {
    negContainer.innerHTML = '<span class="text-gray-500 italic">None</span>';
  }

  // Summary
  document.getElementById('summary-text').innerText = data.summary || 'No summary available.';

  // Top Keywords
  const keyContainer = document.getElementById('keywords-container');
  if (data.top_keywords && data.top_keywords.length > 0) {
    keyContainer.innerHTML = data.top_keywords.map(item => 
      `<span class="px-2.5 py-1 rounded-lg bg-gray-800 text-teal-300 border border-gray-700 text-xs font-medium flex items-center gap-1.5">
        <span>${item.word}</span>
        <span class="px-1.5 py-0.2 rounded bg-gray-900 text-gray-400 text-[10px]">${item.frequency}</span>
      </span>`
    ).join('');
  } else {
    keyContainer.innerHTML = '<span class="text-xs text-gray-500 italic">No significant keywords</span>';
  }
}

// Copy Extractive Summary
function copySummary() {
  const summary = document.getElementById('summary-text').innerText;
  navigator.clipboard.writeText(summary).then(() => {
    alert('Summary copied to clipboard!');
  });
}

// Optimize prompt (Vibe Coding Tab)
async function optimizePrompt() {
  const prompt = document.getElementById('prompt-input').value;
  const domain = document.getElementById('prompt-domain').value;
  const target_audience = document.getElementById('prompt-audience').value;

  if (!prompt.trim()) {
    alert('Please enter a casual prompt or idea first.');
    return;
  }

  try {
    const response = await fetch('/api/optimize-prompt', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, domain, target_audience })
    });

    const result = await response.json();
    if (result.success) {
      document.getElementById('optimized-text').innerText = result.data.raw_optimized;
      document.getElementById('optimized-result-card').classList.remove('hidden');
    }
  } catch (err) {
    console.error('Error optimizing prompt:', err);
    alert('Network error connecting to API.');
  }
}

// Copy optimized prompt
function copyOptimizedPrompt() {
  const text = document.getElementById('optimized-text').innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert('Engineered prompt copied to clipboard!');
  });
}

// Initial health check
async function checkHealth() {
  try {
    const res = await fetch('/api/health');
    const data = await res.json();
    if (data.status === 'healthy') {
      const badge = document.getElementById('health-badge');
      badge.innerText = `Online (${data.uptime_seconds}s)`;
    }
  } catch (e) {
    document.getElementById('health-badge').innerText = 'Offline';
    document.getElementById('health-badge').className = 'text-rose-400 font-medium';
  }
}

// Execute on page load
document.addEventListener('DOMContentLoaded', () => {
  checkHealth();
  setInterval(checkHealth, 15000);
});
