function customSplit(inputString) {
        let indexDot = inputString.indexOf('.', inputString.indexOf('.') + 1);
        let indexSemicolon = inputString.indexOf(';', inputString.indexOf(';') + 1);

        let minIndex = Math.min(indexDot !== -1 ? indexDot : Number.MAX_SAFE_INTEGER,
                                indexSemicolon !== -1 ? indexSemicolon : Number.MAX_SAFE_INTEGER,
                                400);

    return inputString.substring(0, minIndex) + '...';
}

document.addEventListener("DOMContentLoaded", function() {

    let toggleButtons = document.querySelectorAll('.toggle-card');
    toggleButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            let cardContent = this.nextElementSibling;
            if (cardContent.style.display === 'none') {

                const cardId = this.dataset.cardId;
                fetch('https://api.hh.ru/vacancies/' + cardId)
                    .then(response => response.json())
                    .then(data => {
                        const cardContent = this.parentElement.querySelector('.card-content');
                        const desElement = cardContent.querySelector('.description');
                        const skillsElement = cardContent.querySelector('.skills');

                        const des = customSplit(data.description);
                        let res = data.key_skills.map(function (obj){ return obj.name})
                        let skills = res.join(', ');
                        if (!skills){
                            skills = 'отсутствуют'
                        }

                        desElement.innerHTML += des;
                        skillsElement.innerHTML += skills;
                        cardContent.style.display = 'block';
                    });
            } else {
                cardContent.style.display = 'none';
            }
        });
    });
});