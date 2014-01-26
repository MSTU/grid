function OnEnterButton(evt, inputId)
{
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if(charCode == 13)
    {
        checkInput(inputId);
        return false;
    }
}

function checkInput(inputId)
{
    if(document.getElementById(inputId).value =='')
    {
        alert("Please, insert a Name of job!");
        return false;
    }
    else
    {
        editUrl(inputId)
    }
}

function checkJobNameAndRedirect(inputId)
{
    if(document.getElementById(inputId).value =='')
    {
        alert("Please, insert a Name of job!");
        return false;
    }
    else
    {
        create_job.submit();
    }
}

function editUrl(inputId)
{
    url = '/ajax/' + inputId + '/';
    document.getElementById('create_job').action = url;
    create_job.submit();
}

function loadcaseSubmit(inputId) {
    if(document.getElementById(inputId).value =='')
    {
        alert("Please, insert a Name of Loadcase!");
        return false;
    }
    else
    {
        url = '/ajax/' + inputId + '/';
        document.getElementById('create_loadcase').action = url;
        create_loadcase.submit();
    }
}

function modelSubmit(inputId) {
    if(document.getElementById(inputId).value =='')
    {
        alert("Please, insert a Name of Model!");
        return false;
    }
    else
    {
        url = '/ajax/' + inputId + '/';
        document.getElementById('create_model').action = url;
        create_model.submit();
    }
}


function delJob(job_id, job)
{
    if(confirm("Вы уверены, что хотите удалить задачу '" + job() +"'"))
    {
        document.getElementById('del_job').action+= job_id+'/'
        del_job.submit()
    }
}

function checkLength(string , numId)
{
    if(string.length >= 35)
    {
        document.getElementById('jobName_'+ numId).innerHTML = string.substr(0,32) + '...';
    }
}

function setJobName()
{
    curr_date = new Date();
    document.getElementById('addjob').value = 'Job_'+ curr_date.getDate()+ '.' + (curr_date.getMonth()+1) + '.' + curr_date.getFullYear() + '_' + curr_date.getHours() + ":" + curr_date.getMinutes() + ':'+ curr_date.getSeconds();
}

function paginator_url(string)
{
    document.getElementById(string).href='';
}

function addLoadcase(inputId)
{
    if(document.getElementById(inputId).value =='')
    {
        alert("Please, insert a Name of job!");
        return false;
    }
}