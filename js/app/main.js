(function () {
var baseLink = "sambauo7bwpozuhfz.ddns.net";

fetch(baseLink).then(function (response) {
    if (response.ok) {
        response.json().then(function (body) {
            // Pass body to React class, which makes the UI
        });
    } else {
        // Use React to show some error page
    }
});

}());