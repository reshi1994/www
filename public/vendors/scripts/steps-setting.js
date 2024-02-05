import {registerProperty} from '@/store/register'

$(".tab-wizard").steps({
    headerTag: "h5",
    bodyTag: "section",
    transitionEffect: "fade",
    titleTemplate: '<span class="step">#index#</span> #title#',
    labels: {
        finish: "Submit"
    },
    onStepChanged: function (event, currentIndex, priorIndex) {
        $('.steps .current').prevAll().addClass('disabled');
    },
    onFinished: function (event, currentIndex) {
        $('#success-modal').modal('show');
    }
});


const updateRegisterTables = function () {
    let form = $("#register-forms");
    let sections = form.find(`section`)
    sections.each(function (key, element) {
        // console.log(key, element)
        let sectionKey = $(this).attr('name')
        // console.log(console.log(name))
        if (registerProperty.hasOwnProperty(sectionKey)) {
            let inputs = $(this).find('input')
            inputs.each(function (key2, element2) {
                let inputKey = $(this).attr('name')
                console.log(inputKey)
                if (registerProperty[sectionKey].hasOwnProperty(inputKey)) {
                    registerProperty[sectionKey][inputKey] = $(this).val()
                }

            })

        }

    })
}

const updateCurrentTable = function (currentIndex) {
    let form = $("#register-forms");
    let section = form.find(`section`).eq(currentIndex)
    // console.log(key, element)
    let sectionKey = section.attr('name')
    // console.log(sectionKey)
    // console.log(registerProperty.hasOwnProperty(sectionKey))
    if (registerProperty.hasOwnProperty(sectionKey)) {
        let inputs = section.find('input')
        // console.log(inputs)
        inputs.each(function (key2, element2) {
            let inputKey = $(this).attr('name')
            // console.log(inputKey)
            if (registerProperty[sectionKey].hasOwnProperty(inputKey)) {
                // console.log(registerProperty[sectionKey][inputKey])
                registerProperty[sectionKey][inputKey]['value'] = $(this).val()
            }

        })
    }


}



$(".tab-wizard2").steps({
    headerTag: "h5",
    bodyTag: "section",
    transitionEffect: "fade",
    titleTemplate: '<span class="step">#index#</span> <span class="info">#title#</span>',
    labels: {
        finish: "Submit",
        next: "Next",
        previous: "Previous",
    },
    onStepChanging: function (event, currentIndex, priorIndex) {
        updateCurrentTable(currentIndex)
        return true;

    }
    ,
    // onStepChanged: function(event, currentIndex, priorIndex) {
    // 	// console.log(currentIndex, priorIndex)
    // 	$('.steps .current').prevAll().addClass('disabled');
    // },
    onFinished: function (event, currentIndex) {
        $('#success-modal-btn').trigger('click');
    }
});

//定义 获取表格信息的值
