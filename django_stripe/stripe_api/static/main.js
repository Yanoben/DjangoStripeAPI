var id = window.location.href;
var id = Number(id[id.length - 2]);
fetch("/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
        const stripe = Stripe(data.publicKey);

        document.querySelector("#submitBtn").addEventListener("click", () => {
            fetch("/buy/" + id)
                .then((result) => { return result.json(); })
                .then((data) => {
                    console.log(data);
                    return stripe.redirectToCheckout({ sessionId: data.sessionId })
                })
                .then((res) => {
                    console.log(res);
                });
        });
    });