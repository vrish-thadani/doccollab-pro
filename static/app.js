document.addEventListener("DOMContentLoaded", function () {

    const shareBtn =
    document.querySelector(".share-btn");

    if (shareBtn) {

        shareBtn.addEventListener(
            "click",
            function () {

                const email =
                prompt(
                    "Enter collaborator email"
                );

                if(email){

                    fetch(
                        "/share-document",
                        {
                            method:"POST",

                            headers:{
                                "Content-Type":
                                "application/x-www-form-urlencoded"
                            },

                            body:
                            "username=Collaborator&email="
                            +
                            encodeURIComponent(email)
                        }
                    )

                    .then(response=>response.json())

                    .then(data=>{

                        alert(
                            "Document shared successfully with\n\n"
                            + email
                        );

                    });

                }

            }
        );

    }

    const historyBtn =
    document.querySelector(".history-btn");

    if(historyBtn){

        historyBtn.addEventListener(
            "click",
            function(){

                window.location.href =
                "/versions";

            }
        );

    }

    const commentButton =
    document.querySelector(
        ".comment-box button"
    );

    if(commentButton){

        commentButton.addEventListener(
            "click",
            function(){

                const textarea =
                document.querySelector(
                    ".comment-box textarea"
                );

                const value =
                textarea.value.trim();

                if(value === ""){

                    alert(
                        "Enter a comment first"
                    );

                    return;

                }

                fetch(
                    "/add-comment",
                    {
                        method:"POST",

                        headers:{
                            "Content-Type":
                            "application/x-www-form-urlencoded"
                        },

                        body:
                        "username=Vrish Thadani&comment="
                        +
                        encodeURIComponent(value)
                    }
                )

                .then(response=>response.json())

                .then(data=>{

                    alert(
                        "Comment Added Successfully"
                    );

                    location.reload();

                });

            }
        );

    }

    const search =
    document.querySelector(".search");

    if(search){

        search.addEventListener(
            "keyup",
            function(){

                const query =
                this.value.toLowerCase();

                const cards =
                document.querySelectorAll(
                    ".recent-card"
                );

                cards.forEach(function(card){

                    const text =
                    card.innerText.toLowerCase();

                    if(
                        text.includes(query)
                    ){

                        card.style.display =
                        "block";

                    }

                    else{

                        card.style.display =
                        "none";

                    }

                });

            }
        );

    }

    const titleInput =
    document.querySelector(
        ".doc-title"
    );

    if(titleInput){

        titleInput.addEventListener(
            "input",
            function(){

                const status =
                document.querySelector(
                    ".save-status"
                );

                status.innerHTML =
                "Saving...";

                setTimeout(
                    function(){

                        status.innerHTML =
                        "✓ Saved to Cloud";

                    },
                    1000
                );

            }
        );

    }

    const metrics =
    document.querySelectorAll(
        ".metric"
    );

    const page =
    document.querySelector(
        ".document-page"
    );

    if(
        page &&
        metrics.length >= 2
    ){

        const text =
        page.innerText;

        const words =
        text.split(/\s+/).length;

        const chars =
        text.length;

        metrics[0].innerHTML =
        words + " Words";

        metrics[1].innerHTML =
        chars + " Characters";

    }

    const activityCards =
    document.querySelectorAll(
        ".activity-card"
    );

    activityCards.forEach(function(card){

        card.addEventListener(
            "click",
            function(){

                alert(
                    card.innerText
                );

            }
        );

    });

});