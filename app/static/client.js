class Client {
    // == Navigation ==
    static go_to_homepage() {
        window.location.href = "/";
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
