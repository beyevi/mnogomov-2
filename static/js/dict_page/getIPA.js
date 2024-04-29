// const fetch = require('node-fetch');

async function getEngIPA(word) {
    const url = `https://wordsapiv1.p.rapidapi.com/words/${word}/pronunciation`;
    const options = {
      method: 'GET',
      headers: {
        'X-RapidAPI-Key': 'f00a56a03fmshb59ec5f0f1c92b6p1e1854jsnae98d6e68873',
        'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com'
      }
    };
    
    try {
        const response = await fetch(url, options);
        result = await response.json();
        console.log(result.pronunciation.all);
    } catch (error) {
        console.error(error);
    }
}
