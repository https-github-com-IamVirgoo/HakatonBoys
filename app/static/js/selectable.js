$(document).ready(
    () => {
        let v = $('#select-val').val();
        $("#exchange_price").text($("#exchange_price").text().replace('{price}', v));
        
        // ----------------------------------------------------------------
    }
);

// ----------------------------------------------------------------
$(document).ready(() => {
    $("#select-val").change(function () {
        let v = $("#select-val option:selected").val();
        $("#exchange_price").text(v);
        last_val = v;
        alert(1)
        let resp = fetch('/api/v1/' + v, []);
    });
})