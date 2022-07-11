class Client {
    // == Navigation ==
    static go_to_overview() {
        window.location.href = "/";
    }

    static go_to_login() {
        window.location.href = "/login";
    }

    // == Components ==
    static campaign_list(success, failure) {
        const token = sessionStorage.getItem("token");
        $.ajax({
            url: "/components/campaigns",
            type: "GET",
            headers: {
                Authorization: "Bearer " + token,
            },
            success: success,
            error: failure,
        });
    }
}
