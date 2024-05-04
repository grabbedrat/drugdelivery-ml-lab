$(document).ready(function() {
  $('.chat-form').on('submit', function(event) {
    event.preventDefault();

    var chatContainer = $(this).closest('[id^=chat-container]');
    var chatHistory = chatContainer.find('[id^=chat-history]');
    var initialContext = chatContainer.find('[name^=initial_context]');
    var prompt = chatContainer.find('[name^=prompt]');
    var context = chatContainer.find('[name^=context]');

    var initialContextValue = initialContext.val().trim() || initialContext.attr('placeholder');
    var promptValue = prompt.val().trim();

    if (promptValue === '') {
      alert('Please enter a message in the prompt field.');
      return;
    }

    var chatHistoryParagraphs = chatHistory.find('p');
    var contextValue = '';

    // Add initial context to the top of chat history if it's the first submit
    if (chatHistoryParagraphs.length === 0) {
      chatHistory.append('<p><strong>Initial Context:</strong> ' + initialContextValue + '</p>');
      initialContext.val('');
      initialContext.hide();
    }

    chatHistoryParagraphs = chatHistory.find('p');
    chatHistoryParagraphs.each(function() {
      contextValue += $(this).text() + '\n';
    });

    context.val(contextValue);

    var formData = new FormData();
    formData.append(prompt.attr('name'), promptValue);
    formData.append(context.attr('name'), contextValue);

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

document.addEventListener('DOMContentLoaded', function() {
  var toggleButton = document.getElementById('toggle-gist');
  var gistContainer = document.getElementById('gist-container');

  toggleButton.addEventListener('click', function() {
    if (gistContainer.style.display === 'none') {
      gistContainer.style.display = 'block';
      toggleButton.textContent = 'Hide Jupyter Notebook';
    } else {
      gistContainer.style.display = 'none';
      toggleButton.textContent = 'View Jupyter Notebook';
    }
  });
});