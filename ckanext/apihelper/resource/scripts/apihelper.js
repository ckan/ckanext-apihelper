ckan.module('apihelper', function (jQuery, _) {
  return {
    initialize: function () {
      this.el.change(this.change);
    },
    change: function (e) {
      var helparea = $('#apihelper-help');
      var help_text = "Select an endpoint to see it's documentation.";
      // get element only if it exists
      if(action_help[e.val] !== undefined) {
        help_text = action_help[e.val];
      }
      // get the newlines converted properly
      help_text = help_text.replace(/\n/g, '<br />')
      helparea.html(help_text);
    },
  };
});
