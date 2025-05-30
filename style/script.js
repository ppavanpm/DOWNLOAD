document.getElementById('downloadForm').onsubmit = async function (e) {
  e.preventDefault();
  const form = new FormData(this);
  document.getElementById('status').textContent = 'Starting download...';
  document.getElementById('progressBar').value = 0;

  const res = await fetch('/download', {
    method: 'POST',
    body: form
  });
  const { id } = await res.json();

  const checkProgress = async () => {
    const res = await fetch(`/progress/${id}`);
    const data = await res.json();
    document.getElementById('status').textContent = data.status;

    if (data.status.includes('Downloading')) {
      const percent = parseFloat(data.progress);
      document.getElementById('progressBar').value = percent;
      setTimeout(checkProgress, 1000);
    } else if (data.status === 'Done') {
      document.getElementById('progressBar').value = 100;
      document.getElementById('status').textContent = "✅ Done!";
      window.location.href = `/download_file/${id}`;
    } else if (data.status.startsWith('Error')) {
      document.getElementById('status').textContent = data.status;
    } else {
      setTimeout(checkProgress, 1000);
    }
  };

  checkProgress();
};
