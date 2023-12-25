window.onload = function showactive()
{
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
        </table>`

    }
    $.ajax({
        url: '/search',
        type: 'GET',
        success: function (response) {
            
            var students1 = response;
            createTable1(students1);
        }
    })

    const createTableData1 = (students1) => {

        let html1 = ``
        students1.forEach(student => {

            if (student.status == "active") {
                html1 += `
                    <tr id="${student.id}">
                        <td>${student.Fname + ' ' + student.Lname}</td>
                        <td>${student.id}</td>
                        <td>${student.email}</td>
                        <td>${student.level}</td>
                        <td>${student.gpa}</td>
                        <td>
                            <select name="status" id="status" value="${student.status}" onchange="change_activity(${student.id})">
                                <option value="active" id="active" selected="selected">Active</option>
                                <option value="inactive" id="inactive">Inactive</option>
                            </select>
                        </td>
                        <td>${student.phone}</td>
                        <td>${student.dep}</td>
                    </tr>
                `
            } else {
                html1 += `
                    <tr id="${student.id}">
                        <td>${student.Fname + ' ' + student.Lname}</td>
                        <td>${student.id}</td>
                        <td>${student.email}</td>
                        <td>${student.level}</td>
                        <td>${student.gpa}</td>
                        <td>
                            <select name="status" id="status" value="${student.status}" onchange="change_activity(${student.id})">
                                <option value="active" id="active">Active</option>
                                <option value="inactive" id="inactive" selected="selected">Inactive</option>
                            </select>
                        </td>
                        <td>${student.phone}</td>
                        <td>${student.dep}</td>
                    </tr>
                `
            }

        });
        return html1;
    }
}

function change_activity(id) {
    var c = confirm("Are you sure you want to change activity?");
    if (c) {
      var newStatus = document.getElementById("status").value;
  
      $.ajax({
        url: '/update', // Endpoint to update the status in the SQLite database
        type: 'POST',
        data: {
          id: id,
          status: newStatus
        },
        
        success: function (response) {
          alert("Student has been updated");
          // Perform any necessary UI updates or refresh the student list
        },
        error: function (error) {
            console.log(newStatus)
          console.error('Error updating status:', error);
          // Handle the error appropriately
        }
      });
    }
  }
  