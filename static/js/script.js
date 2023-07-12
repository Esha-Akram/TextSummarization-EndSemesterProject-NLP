// This code should be placed in a separate script file (e.g., script.js)

document.addEventListener('DOMContentLoaded', () => {
  const inputText = document.getElementById('input-text');
  const charCount = document.getElementById('char-count');
  const summarizeBtn = document.getElementById('summarize-btn');
  const loadingSpinner = document.getElementById('loading-spinner');
  const originalText = document.getElementById('original-text');
  const summaryText = document.getElementById('summary-text');
  const copyBtn = document.getElementById('copy-btn');
  const rangeInput = document.getElementById('summary-length');
  const rangeValue = document.getElementById('range-value');

  inputText.addEventListener('input', () => {
    charCount.innerText = inputText.value.length;
  });

  rangeInput.addEventListener('input', () => {
    rangeValue.innerText = rangeInput.value + '%';
  });

  summarizeBtn.addEventListener('click', () => {
    if (inputText.value.trim() === '') {
      alert('Please enter some text.');
      return;
    }

    loadingSpinner.classList.remove('hide');
    originalText.innerText = inputText.value;
    summaryText.innerText = '';

    setTimeout(() => {
      const summaryLength = rangeInput.value;
      const input = inputText.value;

      // Simulating delay for demo purposes
      const summary = summarizeText(input, summaryLength);

      summaryText.innerText = summary;
      loadingSpinner.classList.add('hide');
      document.getElementById('output-section').classList.remove('hide');
    }, 2000);
  });

  copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(summaryText.innerText)
      .then(() => {
        alert('Summary copied to clipboard.');
      })
      .catch((error) => {
        console.error('Unable to copy summary:', error);
      });
  });

  function summarizeText(input, summaryLength) {
    // Perform the necessary logic to generate the summary
    // Replace this with your actual summarization algorithm
    const generatedSummary = 'This is a sample summary.';
    const adjustedLength = Math.ceil(generatedSummary.length * (summaryLength / 100));
    const truncatedSummary = generatedSummary.slice(0, adjustedLength) + '...';
    return truncatedSummary;
  }
});
