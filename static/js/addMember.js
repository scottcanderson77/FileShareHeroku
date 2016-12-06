/**
 * Created by Keshav on 11/19/2016.
 */
function addToGroup(username, groupID) {
    $.ajax({
       url : 'https://bestreports.herokuapp.com/addmember/',
       type : 'POST',
       data : { 'username' : username.innerHTML, 'groupID' : groupID },
       success : function (data){
           console.log(data.g_id);
       },
       error : function () {
           alert('Could not make post request')
       }
    });
}

function removeFromGroup(username, groupID) {
    $.ajax({
       url : 'https://bestreports.herokuapp.com/removeMember/',
       type : 'POST',
       data : { 'username' : username.innerHTML, 'groupID' : groupID },
       success : function (data){
           console.log(data.g_id);
       },
       error : function () {
           alert('Could not make post request')
       }
    });
}

function changeRole(username, isSM) {
    $.ajax({
        url : 'https://bestreports.herokuapp.com/updatePrivilege/',
        type : 'POST',
        data : { 'username' : username.innerHTML, 'isSM' : isSM },
        success : function (data){
           console.log(data);
        },
        error : function () {
           alert('Could not make post request')
        }
    });
}