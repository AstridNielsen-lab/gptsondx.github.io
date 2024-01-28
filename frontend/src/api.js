// api.js

const BASE_URL = 'http://localhost:5000'; // Ajuste conforme necessário

export async function rastrearFrequencias() {
  try {
    const response = await fetch(`${BASE_URL}/rastrear_frequencias`);
    if (!response.ok) {
      throw new Error(`Erro ao rastrear frequências. Código: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Erro ao realizar chamada à API:', error.message);
    throw error;
  }
}
