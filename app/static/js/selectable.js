$(document).ready(
    () => {
        let v = $('#select-val').val();
        $("#exchange_price").text(v);
    }
);

$(document).ready(() => {
    // 
    // Sends request to server to get val
    //
    $('#select-val').change(() => {
        let v = $('#select-val').val();
        let resp = fetch('/api/v1/price/' + v)
                .then((r) => r.json())
                .then((data) => {
                    $('#exchange_price').text(data);
        });
    });
});