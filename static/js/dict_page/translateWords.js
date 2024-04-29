async function translateInEnglish(word) {
    const url = `https://google-translate-api8.p.rapidapi.com/google-translate/?text=${word}&lang=en`;
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-RapidAPI-Key': 'f00a56a03fmshb59ec5f0f1c92b6p1e1854jsnae98d6e68873',
            'X-RapidAPI-Host': 'google-translate-api8.p.rapidapi.com'
        },
        body: {
            key1: 'value',
            key2: 'value'
        }
    };

    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
}


async function translateInFrench(word) {
    const url = `https://google-translate-api8.p.rapidapi.com/google-translate/?text=${word}&lang=fr`;
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-RapidAPI-Key': 'f00a56a03fmshb59ec5f0f1c92b6p1e1854jsnae98d6e68873',
            'X-RapidAPI-Host': 'google-translate-api8.p.rapidapi.com'
        },
        body: {
            key1: 'value',
            key2: 'value'
        }
    };

    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
}


async function translateInUkrainian(word) {
    const url = `https://google-translate-api8.p.rapidapi.com/google-translate/?text=${word}&lang=uk`;
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-RapidAPI-Key': 'f00a56a03fmshb59ec5f0f1c92b6p1e1854jsnae98d6e68873',
            'X-RapidAPI-Host': 'google-translate-api8.p.rapidapi.com'
        },
        body: {
            key1: 'value',
            key2: 'value'
        }
    };

    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
}