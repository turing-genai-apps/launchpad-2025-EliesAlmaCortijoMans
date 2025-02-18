import React, { useState } from 'react';
import axios from 'axios';

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const sendMessage = async (e) => {
        e.preventDefault();
        if (!input.trim()) return;

        const userMessage = input;
        setInput('');
        setMessages(prev => [...prev, { text: userMessage, isUser: true }]);
        setIsLoading(true);

        try {
            const response = await axios.post('http://localhost:8000/chat', {
                message: userMessage
            });

            setMessages(prev => [...prev, { text: response.data.response, isUser: false }]);
        } catch (error) {
            console.error('Error:', error);
            setMessages(prev => [...prev, { text: 'Error: Could not get response', isUser: false }]);
        }

        setIsLoading(false);
    };

    return (
        <div className="chat-container">
            <div className="messages">
                {messages.map((message, index) => (
                    <div key={index} className={`message ${message.isUser ? 'user' : 'agent'}`}>
                        {message.text}
                    </div>
                ))}
                {isLoading && <div className="message agent">Thinking...</div>}
            </div>
            <form onSubmit={sendMessage} className="input-form">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type your message..."
                    disabled={isLoading}
                />
                <button type="submit" disabled={isLoading}>Send</button>
            </form>
        </div>
    );
};

export default Chat;