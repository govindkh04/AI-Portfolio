const API_URL = "http://127.0.0.1:8000";


// --------------------------------------------------
// Get HTML elements
// --------------------------------------------------

const chatContainer = document.getElementById("chat-container");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

const quickQuestions =
    document.querySelectorAll(".quick-question");

const jobFitButton =
    document.getElementById("job-fit-button");

const jobFileInput =
    document.getElementById("job-file-input");

const jobFitResult =
    document.getElementById("job-fit-result");


// --------------------------------------------------
// Add a message to the chat
// --------------------------------------------------

function addMessage(text, type) {

    const message = document.createElement("div");

    message.classList.add(
        "message",
        `${type}-message`
    );

    const avatar = document.createElement("div");

    avatar.classList.add("message-avatar");

    avatar.textContent =
        type === "assistant" ? "G" : "You";

    const content = document.createElement("div");

    content.classList.add("message-content");

    content.textContent = text;

    message.appendChild(avatar);
    message.appendChild(content);

    chatContainer.appendChild(message);

    chatContainer.scrollTop =
        chatContainer.scrollHeight;
}


// --------------------------------------------------
// Send chat message
// --------------------------------------------------

async function sendMessage() {

    const message =
        messageInput.value.trim();

    if (!message) {
        return;
    }

    // Display user's message
    addMessage(message, "user");

    // Clear input
    messageInput.value = "";

    // Disable button while waiting
    sendButton.disabled = true;
    sendButton.textContent = "...";

    try {

        const response = await fetch(
            `${API_URL}/chat`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );


        if (!response.ok) {
            throw new Error(
                "Failed to get response from server."
            );
        }


        const data = await response.json();


        // Display AI response
        addMessage(
            data.response,
            "assistant"
        );


    } catch (error) {

        console.error(error);

        addMessage(
            "Sorry, I couldn't connect to the AI right now.",
            "assistant"
        );

    } finally {

        sendButton.disabled = false;
        sendButton.textContent = "➤";
    }
}


// --------------------------------------------------
// Send button
// --------------------------------------------------

sendButton.addEventListener(
    "click",
    sendMessage
);


// --------------------------------------------------
// Enter key
// --------------------------------------------------

messageInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendMessage();
        }
    }
);


// --------------------------------------------------
// Quick questions
// --------------------------------------------------

quickQuestions.forEach(
    function(button) {

        button.addEventListener(
            "click",
            function() {

                const question =
                    button.dataset.question;

                messageInput.value = question;

                sendMessage();
            }
        );
    }
);


// --------------------------------------------------
// Job fit button
// --------------------------------------------------

jobFitButton.addEventListener(
    "click",
    function() {

        jobFileInput.click();
    }
);


// --------------------------------------------------
// Job description upload
// --------------------------------------------------

jobFileInput.addEventListener(
    "change",
    async function() {

        const file =
            jobFileInput.files[0];

        if (!file) {
            return;
        }


        jobFitButton.disabled = true;
        jobFitButton.textContent = "Analyzing...";

        jobFitResult.classList.remove("hidden");

        jobFitResult.innerHTML =
            "<p>Analyzing the job description...</p>";


        try {

            const formData = new FormData();

            formData.append(
                "file",
                file
            );


            const response = await fetch(
                `${API_URL}/job-fit`,
                {
                    method: "POST",
                    body: formData
                }
            );


            if (!response.ok) {
                throw new Error(
                    "Job fit request failed."
                );
            }


            const data =
                await response.json();


            displayJobFitResult(data);


        } catch (error) {

            console.error(error);

            jobFitResult.innerHTML =
                "<p>Could not analyze the job description.</p>";

        } finally {

            jobFitButton.disabled = false;
            jobFitButton.textContent = "Check Job Fit";

            jobFileInput.value = "";
        }
    }
);


// --------------------------------------------------
// Display job-fit result
// --------------------------------------------------

function displayJobFitResult(data) {

    const matchingSkills =
        data.matching_skills
            .map(skill => `<li>${skill}</li>`)
            .join("");

    const missingSkills =
        data.missing_skills
            .map(skill => `<li>${skill}</li>`)
            .join("");


    jobFitResult.innerHTML = `
        <h3>Job Fit Analysis</h3>

        <div class="match-percentage">
            ${data.match_percentage}%
        </div>

        <p><strong>Matching Skills</strong></p>

        <ul>
            ${matchingSkills || "<li>None identified</li>"}
        </ul>

        <p><strong>Missing Skills</strong></p>

        <ul>
            ${missingSkills || "<li>None identified</li>"}
        </ul>

        <p><strong>Overall Assessment</strong></p>

        <p>
            ${data.reason}
        </p>
    `;
}