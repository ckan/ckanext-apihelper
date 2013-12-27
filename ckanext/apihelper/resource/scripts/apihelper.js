ckan.module('apihelper', function (jQuery, _) {
  return {
    initialize: function () {
      this.el.change(this.change);
    },
    change: function (e) {
      var helparea = $('#apihelper-help');
      var help_text = "";
      // get element only if it exists
      if(-1 <= $.inArray(e.val, action_help)) {
        help_text = action_help[e.val];
      }
      // some basic formatting
      help_text = help_text.replace(/\n/g, '<br />')
      helparea.html(help_text);
    },
  };
});
