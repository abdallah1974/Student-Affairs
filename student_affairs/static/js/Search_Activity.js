const createTableData1 = (student) => {

    let html1 = ` 
    <tr>
        <td>${student.Fname + ' ' + student.Lname}</td>
        <td>${student.id}</td>
        <td>${student.email}</td>
        <td>${student.level}</td>
        <td>${student.gpa}</td>
        <td>${student.status}</td>
        <td>${student.phone}</td>
        <td>${student.dep}</td>
    </tr>
    `


    return html1;
}

function search() {
    var target = document.getElementById("Fname").value;

    $.ajax({
        url: '/search',
        type: 'GET',
        data: {
            name: target
        },
        success: function (response) {
            document.getElementById('results').innerHTML = '';

            var found = false;
            const all = response;
            // console.log(all);
            // console.log(target)
            // console.log(all[0].Fname)
            for (var i = 0; i < all.length; i++) {
                if (all[i].Fname == target) {
                    document.getElementById('results').innerHTML += createTableData1(all[i]);
                    found = true;
                }
            }
            if (!found && target !== '') {
                alert('Student not found...try another name');
            }
        }
    })
}