class Client {
    // == Navigation ==
    static go_to_overview() {
        window.location.href = "/";
    }

    static go_to_login() {
        window.location.href = "/login";
    }

    static go_to_new_campaign(name) {
        window.location.href = "/new_campaign/" + String(name);
    }

    static go_to_campaign(name) {
        window.location.href = "/campaign/" + String(name);
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

    // == Campaign ==
    static create_campaign(name, inputs, outputs, success, failure) {
        console.log(inputs);
        const token = sessionStorage.getItem("token");
        $.ajax({
            url: "/create_campaign/" + String(name),
            type: "POST",
            headers: {
                Authorization: "Bearer " + token,
            },
            contentType: "application/json",
            data: JSON.stringify({
                inputs: inputs,
                outputs: outputs,
            }),
            success: success,
            error: failure,
        });
    }

    //static create_campaign(name, inputs, outputs, success, failure) {
    //    const token = sessionStorage.getItem("token");
    //    $.ajax({
    //        url: "/create_campaign/" + String(name),
    //        type: "POST",
    //        headers: {
    //            Authorization: "Bearer " + token,
    //        },
    //        contentType: "application/json",
    //        data: JSON.stringify({
    //            inputs: inputs[0],
    //            input_mins: inputs[1],
    //            input_maxs: inputs[2],
    //            outputs: outputs[0],
    //            output_mins: outputs[1],
    //            output_maxs: outputs[2],
    //        }),
    //        success: success,
    //        error: failure,
    //    });
    //}
}
