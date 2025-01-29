import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000"; // Backend URL

export const sendMessageToBot = async (message) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/chat`, { message });
        return response.data.response; // Extract response from API
    } catch (error) {
        console.error("Error communicating with backend:", error);
        return "Error: Unable to reach chatbot.";
    }
};
