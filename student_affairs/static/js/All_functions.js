var activeStudentsArray = JSON.parse(localStorage.getItem("data")) || [];


function find(array, studentData) {
    for (var i = 0; i < array.length; i++) {
        if (array[i].id == studentData.id || array[i].email == studentData.email) {
            return array[i];


        }
    }
   
    return false;
}


function check_level(){
    var level = document.getElementById("level").value;
    if (level < 3) {
        document.getElementById("dep").value = "General";
        document.getElementById("dep").disabled = true;

    } else {
        document.getElementById("dep").disabled = false;

    }
}
window.onload = check_level;


function savedata() {
    var id = document.getElementById("id").value;
    var Fname = document.getElementById("Fname").value;
    var Lname = document.getElementById("Lname").value;
    var date = document.getElementById("date").value;
    var gpa = document.getElementById("gpa").value;
    var gender = document.getElementById("gender").value;
    var level = document.getElementById("level").value;
    var status = document.getElementById("status").value; 
    var email = document.getElementById("email").value;
    var phone = document.getElementById('phone').value;
    var department = document.getElementById("dep").value;   
}

function SignIn() {
    var id = document.getElementById("id").value;
    var email = document.getElementById("email").value;

    var user = {
        id: id,
        email : email
    }
   
    var regestired = Object.assign({}, find(activeStudentsArray, user));

    if (user.id != '' && user.email != '') {
        if (find(activeStudentsArray, user)) {

            if (user.id != regestired.id || user.email != regestired.email) {
                alert("No Matching between ID and Email , plz try again");
            } else {

                window.location.href = 'Update_Info.html';
                window.localStorage.setItem("regestired", JSON.stringify(regestired));


            }
        } else {
            alert("There is no user with this data, plz try again");
        }
    }
}


function removeStudent() {
    var id = document.getElementById("id").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{% url 'remove_student' student_id=id %}", true);
    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
    xhr.send();
}


function resetFormFields() {
    document.getElementById("gpa").value = "0";
    document.getElementById("level").value = "1";
    document.getElementById("status").value = "Active";
    document.getElementById("email").value = "";
    document.getElementById("phone").value = ""; 
}


