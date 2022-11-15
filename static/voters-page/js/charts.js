// line chart


// doughnut chart
document.addEventListener("DOMContentLoaded", () => {
    new Chart(document.querySelector('#votersChart'), {
        type: 'doughnut',
        data: {
        labels: [
            {% if male_reg_voters %}'Male(s)',{% endif %} {% if female_reg_voters %}'Female(s)'{% endif %}
        ],
        datasets: [{
            label: 'Registered Voters',
            data: [
                {{male_reg_voters}}, {{female_reg_voters}}
            ],
            backgroundColor: [
                '#09ac52',
                '#ec0b0b',
            ],
            hoverOffset: 4,
        }]
        }
    });
});
