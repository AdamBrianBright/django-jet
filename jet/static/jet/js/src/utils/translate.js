module.exports = function(str) {
    if (window.django == undefined) {
        return str;
    }
    try {
        return django.gettext(str);
    } catch(err) {
        return gettext(str);
    }
};
