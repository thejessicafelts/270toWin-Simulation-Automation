// JavaScript for Tab Functionality and Loading Code
document.addEventListener("DOMContentLoaded", () => {
    const tabButtons = document.querySelectorAll(".tab-button");
    const tabContents = document.querySelectorAll(".tab-content");
    const copyButton = document.getElementById("copy-button");

    tabButtons.forEach(button => {
        button.addEventListener("click", () => {
            tabButtons.forEach(btn => btn.classList.remove("active"));
            tabContents.forEach(content => content.classList.remove("active"));

            button.classList.add("active");
            document.getElementById(button.dataset.tab).classList.add("active");

            if (button.dataset.tab === "code-tab") {
                loadScriptCode();
            }
        });
    });

    function loadScriptCode() {
        const codeElement = document.getElementById("script-code");
        if (!codeElement.textContent) {
            fetch('path/to/your_script.py') // Replace with the actual path to your Python script file
                .then(response => response.text())
                .then(code => {
                    codeElement.textContent = code;
                })
                .catch(error => console.error("Error loading script code:", error));
        }
    }

    // Copy Button
    document.addEventListener("DOMContentLoaded", () => {
        const copyButtons = document.querySelectorAll(".copy-button");
    
        copyButtons.forEach(button => {
            button.addEventListener("click", () => {
                const codeElement = button.closest(".code-block").querySelector("code");
                navigator.clipboard.writeText(codeElement.textContent)
                    .then(() => {
                        button.textContent = "Copied!";
                        setTimeout(() => {
                            button.textContent = "Copy";
                        }, 2000);
                    })
                    .catch(error => console.error("Copy failed:", error));
            });
        });
    });
    
});
