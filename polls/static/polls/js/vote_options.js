// let survey_options = document.getElementById('poll_options');
// let add_more_fields = document.getElementById('add_more_fields');
// let remove_fields = document.getElementById('remove_fields');
let x = 0

function add_more_fields() {
    let poll_options = document.getElementById('poll_options');
    // alert("worked");
    let newField = document.createElement('input');
    x++;
    newField.setAttribute('type', 'text');
    let option_id = new String('option_' + x)
    newField.setAttribute('name', option_id);
    newField.setAttribute('class', 'survey_options');
    // newField.setAttribute('siz',50);
    newField.setAttribute('placeholder', 'Another Field');
    poll_options.appendChild(newField);
}

// remove_fields.onclick = function(){
//   var input_tags = survey_options.getElementsByTagName('input');
//   if(input_tags.length > 2) {
//     survey_options.removeChild(input_tags[(input_tags.length) - 1]);
//   }
// }