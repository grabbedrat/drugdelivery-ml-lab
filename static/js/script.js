$(document).ready(function() {
  var initialContext = $('textarea[name="initial_context"]');
  var chatHistory = $('#chat-history');
  var prompt = $('textarea[name="prompt"]');

  $('#chat-form').on('submit', function(event) {
    event.preventDefault();

    var initialContextValue = initialContext.val().trim() || initialContext.attr('placeholder');
    var promptValue = prompt.val().trim();

    if (promptValue === '') {
      alert('Please enter a message in the prompt field.');
      return;
    }

    var chatHistoryParagraphs = chatHistory.find('p');
    var context = '';

    // Add initial context to the top of chat history if it's the first submit
    if (chatHistoryParagraphs.length === 0) {
      chatHistory.append('<p><strong>Initial Context:</strong> ' + initialContextValue + '</p>');
      initialContext.val('');
      initialContext.hide();
    }

    chatHistoryParagraphs = chatHistory.find('p');
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
        prompt.val('');
      },
      error: function() {
        alert('An error occurred while submitting the form.');
      }
    });
  });
});