$(document).ready(
    () => {
        let v = $('#select-val').val();
        $("#exchange_price").text(v);
        // ----------------------------------------------------------------
    }
);

// ----------------------------------------------------------------
$(document).ready(() => {
    $("#select-val").change(function () {
        let v = $("#select-val option:selected").val();
        last_val = v;
        let resp = fetch('/api/v1/price/' + v, [])
            .then((resp) => resp.json())
            .then(function(data) {
                $("#exchange_price").text(data.content);
                alert(data.content)
        });
    });
})