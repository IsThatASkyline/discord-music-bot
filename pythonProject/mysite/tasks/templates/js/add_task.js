              $(document).ready(function () {

                  $('#myForm').submit(function () {
                      $.ajax({
                          data: $(this).serialize(),
                          type: $(this).attr('method'),
                          url: "{% url 'category' category_id %}",
                          success: function (json) {
                            document.getElementById("myForm").reset();
                            $("#tasks").prepend(
                             '<a class="a_'+json.new_task_id+'" href="/'+json.category_id+'/'+json.new_task_id+'/details">' +
                                '<div class="card-body rounded text">' +
                                   '<div class="form-check">' +
                                      '<input class="form-check-input" type="checkbox" name="'+json.new_task_id+'">' +
                                       json.title +
                                    '</div>' +
                                '</div>' +
                             '</a>'
                            )
                            },


                          error: function (response) {

                              alert(response.responseJSON.errors);
                              console.log(response.responseJSON.errors)
                          }
                      });
                      return false;
                  });
              })
