$(document).ready(function() {
    $('#chat-form').on('submit', function(event) {
      event.preventDefault();
  
      var chatHistory = $('#chat-history');
      var chatHistoryParagraphs = chatHistory.find('p');
      var context = '';
  
      chatHistoryParagraphs.each(function() {
        context += $(this).text() + '\n';
      });
  
      $('input[name="context"]').val(context);
  
      var formData = new FormData(this);
  
      $.ajax({
        type: 'POST',
        url: '/chatbot',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          chatHistory.append('<p>' + response + '</p>');
          $('#chat-form textarea[name="prompt"]').val('');
        },
        error: function() {
          alert('An error occurred while submitting the form.');
        }
      });
    });
  });