document.addEventListener('DOMContentLoaded', function() {
  let count = 0;
  let interval = setInterval(function() {
    count++;
    console.log(count);
    if (count >= 1000000) {
      clearInterval(interval);
    }
  }, 1);
});

