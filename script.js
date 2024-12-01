document.addEventListener('DOMContentLoaded', function() {
  let count = 0;
  let interval = setInterval(function() {
    count++;
    console.log(count);
    if (count >= 10000001) {
      clearInterval(interval);
    }
  }, 1);
});

