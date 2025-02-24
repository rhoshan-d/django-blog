setTimeout(function() {
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        alert.classList.remove('show');
        alert.classList.add('hide');
    });
}, 3000);