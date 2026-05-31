function quickAsk(text) {
    const inputField = document.getElementById('user-input');
    inputField.value = text;
    sendMessage();
}

async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const question = input.value.trim();

    if (!question) return;

    chatBox.innerHTML += `<div class="message user">${question}</div>`;
    input.value = '';
    
    const loadingId = 'loading-' + Date.now();
    chatBox.innerHTML += `<div id="${loadingId}" class="message bot">Thinking... ⏳</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch('https://movies-backend-v2.onrender.com/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();
        document.getElementById(loadingId).remove();
        chatBox.innerHTML += `<div class="message bot">${data.answer}</div>`;
    } catch (error) {
        document.getElementById(loadingId).remove();
        chatBox.innerHTML += `<div class="message bot" style="background: #e50914;">Backend error! Is Uvicorn running?</div>`;
    }
    chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') { sendMessage(); }
});

// --- VOICE SEARCH ---
function startVoiceRecognition() {
    const micBtn = document.getElementById('mic-btn');
    const inputField = document.getElementById('user-input');
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    
    if (!SpeechRecognition) {
        alert("Browser not supported.");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.onstart = () => {
        micBtn.classList.add("recording");
        inputField.placeholder = "Listening...";
    };
    recognition.onresult = (event) => {
        inputField.value = event.results[0][0].transcript;
    };
    recognition.onerror = () => { micBtn.classList.remove("recording"); };
    recognition.onend = () => {
        micBtn.classList.remove("recording");
        inputField.placeholder = "Ask about movies...";
    };
    recognition.start();
}

// --- 100% BULLETPROOF: DOWNLOAD CHAT FUNCTION ---
function downloadChat() {
    const chatBox = document.getElementById('chat-box');
    const messages = chatBox.querySelectorAll('.message');
    
    // 1. Screen ko manipulate karne ke bajaye, direct ek HTML string banayen
    let htmlContent = `
        <div style="font-family: Arial, sans-serif; padding: 20px; color: #000000; background-color: #ffffff;">
            <h2 style="text-align: center; border-bottom: 2px solid #000000; padding-bottom: 10px; color: #000000;">
                🎬 Movies Lore Expert - Recommendations
            </h2>
    `;
    
    // 2. Chat ke har message ko naye inline style ke sath string mein add karein
    messages.forEach(msg => {
        const isBot = msg.classList.contains('bot');
        const role = isBot ? "AI Expert" : "You";
        const bgColor = isBot ? "#f9f9f9" : "#e3f2fd";
        
        htmlContent += `
            <div style="background-color: ${bgColor}; padding: 15px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #cccccc; font-size: 14px; line-height: 1.6; color: #000000;">
                <strong style="color: #000000;">${role}:</strong><br><br>
                ${msg.innerHTML}
            </div>
        `;
    });
    
    htmlContent += `</div>`;
    
    const opt = {
        margin:       0.5,
        filename:     'Movies_Lore_Expert_Recommendations.pdf',
        image:        { type: 'jpeg', quality: 1 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    
    // 3. Raw string ko seedha PDF generator ko de dein
    html2pdf().set(opt).from(htmlContent).save();
}