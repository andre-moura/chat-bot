// Get the chat input field and the send button
const inputField = document.getElementById('chat-input-field');
const sendButton = document.getElementById('chat-send-button');

// Get the chat messages container
const messagesContainer = document.getElementById('chat-messages');

// Add event listener to the input field
inputField.addEventListener('keyup', (event) => {
    // If the key pressed is the enter key
    if (event.key == 'Enter') {
        // Trigger the send button click event
        sendButton.click();

        // Prevent the default behavior of the enter key
        event.preventDefault();
    }
});


// Add event listener to the send button
sendButton.addEventListener('click', () => {
    // Get the text from the input field
    const text = inputField.value;

    if (text.trim() != '') {
        // Create a new message div
        const message = document.createElement('span');
        const breakLine = document.createElement('br');

        message.classList.add('chat-message');
        message.textContent = text;

        // Add the message div to the messages container
        messagesContainer.appendChild(breakLine);
        messagesContainer.appendChild(message);

        // Clear the input field
        inputField.value = '';

        // Scroll to the bottom of the messages container
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
});