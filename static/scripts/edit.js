
    $(document).ready(function() {
        $(".edit_bio").change(function () {
            var ID = $(this).attr('id');
            var val = $("#bio_input_" + ID).val();
            var dataString = 'id=' + ID + '&val=' + val;
            if (ID == 'email') {
                
                if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(val)) {
                    ;
                } else {
                    alert("You have entered an invalid email address!");
                    return;
                }
            }
            if (ID == 'phone') {
                if (val.length == 10) {
                    ;
                } else {
                    alert("You have entered an invalid Phone Number!");
                    return;
                }
            }
            //$("#first_" + ID).html('<img src="/staticf/img/loader.gif" />');
            if (val.length > 0) {
                $.ajax({
                    type: "POST",
                    url: "/edit_bio",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        alert('Updated');
                        window.location.reload();
                    }
                });
            } else {
                alert('Enter something.');
            }
        });
        $(".edit_education").change(function () {
            var ID = $(this).attr('id');
            var val1 = $("#id_" + ID).val();
            var val2 = $("#institute_" + ID).val();
            var val3 = $("#course_" + ID).val();
            var val4 = $("#gpa_" + ID).val();
            var dataString = 'id=' + val1 + '&institute=' + val2 + '&course=' + val3 + '&gpa=' + val4;
            //$("#first_" + ID).html('<img src="/staticf/img/loader.gif" />');
            if (val1.length > 0 && val2.length > 0 && val3.length > 0 && val4.length > 0) {
                $.ajax({
                    type: "POST",
                    url: "/edit_education",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        alert('Updated');
                        window.location.reload();
                    }
                });
            } else {
                alert('Enter something.');
            }
        });
        $(".edit_acheivements").change(function () {
            var ID = $(this).attr('id');
            var val1 = $("#experience_" + ID).val();
            var val2 = $("#gate_" + ID).val();
            var val3 = $("#leetcode_" + ID).val();
            var dataString = 'experience=' + val1 + '&gate=' + val2 + '&leetcode=' + val3;
            //$("#first_" + ID).html('<img src="/staticf/img/loader.gif" />');
            if (val1.length > 0 && val2.length > 0 && val3.length > 0) {
                $.ajax({
                    type: "POST",
                    url: "/edit_acheivements",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        alert('Updated');
                        window.location.reload();
                    }
                });
            } else {
                alert('Enter something.');
            }
        });
        $(".edit_experience").change(function () {
            var ID = $(this).attr('id');
            var val1 = $("#description_" + ID).val();
            var val2 = $("#id_" + ID).val();
            var dataString = 'description=' + val1 + '&id=' + val2;
            //$("#first_" + ID).html('<img src="/staticf/img/loader.gif" />');
            if (val1.length > 0) {
                $.ajax({
                    type: "POST",
                    url: "/edit_experience",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        alert('Updated');
                        window.location.reload();
                    }
                });
            } else {
                alert('Enter something.');
            }
        });
        $(".edit_project").change(function () {
            var ID = $(this).attr('id');
            var val1 = $("#id_" + ID).val();
            var val2 = $("#title_" + ID).val();
            var val3 = $("#about_" + ID).val();
            var dataString = 'id=' + val1 + '&title=' + val2 + '&about=' + val3;
            //$("#first_" + ID).html('<img src="/staticf/img/loader.gif" />');
            if (val2.length > 0 && val3.length > 0) {
                $.ajax({
                    type: "POST",
                    url: "/edit_project",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        alert('Updated');
                        window.location.reload();
                    }
                });
            } else {
                alert('Enter something.');
            }
        });
        $(".edit_skills").change(function () {
            var val1 = $("#cpp").val();
            var val2 = $("#java").val();
            var val3 = $("#html").val();
            var val4 = $("#python").val();
            var val5 = $("#php").val();
            var val6 = $("#mysql").val();
            var dataString = 'cpp=' + val1 + '&java=' + val2 + '&html=' + val3 + '&python=' + val4 + '&php=' + val5 + '&mysql=' +val6;
            //$("#first_" + ID).html('<img src="/staticf/img/loader.gif" />');
            if (val1.length > 0 && val2.length > 0 && val3.length > 0 && val4.length > 0 && val5.length > 0 && val6.length > 0) {
                $.ajax({
                    type: "POST",
                    url: "/edit_skills",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        alert('Updated');
                        window.location.reload();
                    }
                });
            } else {
                alert('Enter something.');
            }
        });
    });
