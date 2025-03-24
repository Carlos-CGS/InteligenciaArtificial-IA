const { Configuration, OpenAIApi } = require('openai');
require('dotenv').config();

module.exports = class openai {
  static configuration() {
    if (!process.env.OPENAI_API_KEY) {
      throw new Error('A chave da API do OpenAI (OPENAI_API_KEY) não está definida no arquivo .env');
    }
    const configuration = new Configuration({
      apiKey: process.env.OPENAI_API_KEY,
    });

    return new OpenAIApi(configuration);
  }

  static textCompletion({ prompt }) {
    return {
      model: 'text-davinci-003',
      prompt: `${prompt}`,
      temperature: 0,
      max_tokens: 3500,
      top_p: 1,
      frequency_penalty: 0.5,
      presence_penalty: 0,
    };
  }

  static async chatCompletion(userMessages) {
    const systemMessage = {
      role: 'system',
      content: 'Você é o JARVIS, o assistente virtual do Homem de Ferro. Responda de forma educada, eficiente e com um tom profissional.',
    };

    const chatMessages = [systemMessage, ...userMessages];

    try {
      const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        },
        body: JSON.stringify({
          model: 'gpt-3.5-turbo',
          messages: chatMessages,
        }),
      });

      if (!response.ok) {
        throw new Error(`Erro na API do OpenAI: ${response.status} - ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Erro ao chamar a API do OpenAI:', error.message);
      throw error;
    }
  }
};
