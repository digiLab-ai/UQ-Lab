class Client {
    // == Navigation ==
    static go_to_overview(username) {
        window.location.href = "/overview/" + username;
    }

    static go_to_login(username, name) {
        window.location.href = "/login";
    }

    static go_to_campaign(username, name) {
        window.location.href = "/campaign/" + username + "/" + name;
    }

    // == User ==
    static validate_credentials(username, password, success) {
        $.ajax({
            url: "/validate_credentials/" + username + "/" + password,
            type: "GET",
            success: success,
        });
    }
}
