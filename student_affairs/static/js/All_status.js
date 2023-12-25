window.onload = function showactive() {
    const createTable1 = (students1) => {
        document.getElementById("activetable").innerHTML = `
            <table class="ActiveStudents">
            <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">ID</th>
                <th scope="col">Email</th>
                <th scope="col">Level</th>
                <th scope="col">Gpa</th>
                <th scope="col">Status</th>
                <th scope="col">Phone</th>
                <th scope="col">Dep</th>
            </tr>
            </thead>
            <tbody>
            ${createTableData1(students1)}
            </tbody>
            </table>`;
    };

    $.ajax({
        url: '/search',
        type: 'GET',
        success: function (response) {
            var students1 = response;
            createTable1(students1);
        }
    });

    const createTableData1 = (students1) => {
        let html1 = '';
        students1.forEach(student => {
            if (student.status == 'active') {
                html1 += `
                    <tr id="${student.id}">
                        <td>${student.Fname} ${student.Lname}</td>
                        <td>${student.id}</td>
                        <td>${student.email}</td>
                        <td>${student.level}</td>
                        <td>${student.gpa}</td>
                        <td>
                            <select name="status" id="status_${student.id}" onchange="change_activity(${student.id})">
                                <option value="active" id="active" selected="selected">Active</option>
                                <option value="inactive" id="inactive">Inactive</option>
                            </select>
                        </td>
                        <td>${student.phone}</td>
                        <td>${student.dep ? student.dep : 'General'}</td>
                    </tr>`;
            } else {
                html1 += `
                    <tr id="${student.id}">
                        <td>${student.Fname} ${student.Lname}</td>
                        <td>${student.id}</td>
                        <td>${student.email}</td>
                        <td>${student.level}</td>
                        <td>${student.gpa}</td>
                        <td>
                            <select name="status" id="status_${student.id}" onchange="change_activity(${student.id})">
                                <option value="active" id="active">Active</option>
                                <option value="inactive" id="inactive" selected="selected">Inactive</option>
                            </select>
                        </td>
                        <td>${student.phone}</td>
                        <td>${student.dep ? student.dep : 'General'}</td>
                    </tr>`;
            }
        });
        return html1;
    };
};



function change_activity(id) {
    var c = confirm("Are you sure you want to change the activity?");

    if (c) {
        var statusElement = document.getElementById(`status_${id}`);
        var status = statusElement.value;
        console.log(status);
        var csrftoken = getCSRFToken();

        $.ajax({
            url: '/update_status/',
            type: 'POST',
            data: {
                id: id,
                status: status
            },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function (response) {
                alert("Status has been updated successfully");
            },
            error: function (xhr, status, error) {
                console.log(status)
                alert("Error updating status: " + error);
            }
        });
    }
}

function getCSRFToken() {
    var cookieValue = null;
    var name = "csrftoken";
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
    return cookieValue;
}