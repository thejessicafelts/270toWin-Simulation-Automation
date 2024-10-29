document.addEventListener("DOMContentLoaded", () => {
    const tabButtons = document.querySelectorAll(".tab-button");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach(button => {
        button.addEventListener("click", () => {
            tabButtons.forEach(btn => btn.classList.remove("active"));
            tabContents.forEach(content => content.classList.remove("active"));

            button.classList.add("active");
            document.getElementById(button.dataset.tab).classList.add("active");
        });
    });

    // Copy code to clipboard functionality
    document.querySelectorAll(".copy-button").forEach(button => {
        button.addEventListener("click", () => {
            // Locate the <code> element within the same .code-block container
            const codeElement = button.closest(".code-block").querySelector("code");
            const codeText = codeElement.textContent;

            // Copy the code text to the clipboard
            navigator.clipboard.writeText(codeText)
                .then(() => {
                    button.textContent = "Copied!";
                    setTimeout(() => {
                        button.textContent = "Copy";
                    }, 2000);
                })
                .catch(error => console.error("Failed to copy text:", error));
        });
    });
});
