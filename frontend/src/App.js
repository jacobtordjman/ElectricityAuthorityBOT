import React, { useState } from "react";
import { sendMessageToBot } from "./api";

function App() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const handleSendMessage = async () => {
        if (!input.trim()) return;

        const userMessage = { sender: "user", text: input };
        setMessages([...messages, userMessage]);

        // Send message to backend
        const botResponse = await sendMessageToBot(input);
        setMessages([...messages, userMessage, { sender: "bot", text: botResponse }]);

        setInput("");
    };

    return (
        <div style={{ width: "400px", margin: "auto", padding: "20px", border: "1px solid #ddd", borderRadius: "10px" }}>
            <h2>Chatbot</h2>
            <div style={{ minHeight: "300px", border: "1px solid #ccc", padding: "10px", overflowY: "auto", marginBottom: "10px" }}>
                {messages.map((msg, index) => (
                    <div key={index} style={{ textAlign: msg.sender === "user" ? "right" : "left" }}>
                        <strong>{msg.sender === "user" ? "You" : "Bot"}:</strong> {msg.text}
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type a message..."
                style={{ width: "80%", padding: "10px" }}
            />
            <button onClick={handleSendMessage} style={{ width: "18%", padding: "10px", marginLeft: "2%" }}>
                Send
            </button>
        </div>
    );
}

export default App;
