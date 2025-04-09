document.getElementById("submit-button").addEventListener("click", function () {
    const diet = document.getElementById("diet-input").value;

    fetch("/get_recipes", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ diet: diet })
    })
    .then(response => response.json())
    .then(data => {
        const recipeList = document.getElementById("recipe-list");
        recipeList.innerHTML = "";

        data.recipes.forEach(recipe => {
            const li = document.createElement("li");
            li.textContent = recipe;
            recipeList.appendChild(li);
        });
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
