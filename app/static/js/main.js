document.addEventListener('DOMContentLoaded', function() {
    
    function setupToggle(toggleId, inputId) {
        const toggle = document.getElementById(toggleId);
        const input = document.getElementById(inputId);

        if (toggle && input) {
            function updateInputState() {
                input.disabled = !toggle.checked;
            }
            updateInputState();
            toggle.addEventListener('change', updateInputState);
        }
    }
    setupToggle('use_slag', 'slag');
    setupToggle('use_fly_ash', 'fly_ash');
    setupToggle('use_superplasticizer', 'superplasticizer');
});