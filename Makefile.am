EXTRA_DIST = \
	rollo \
	COPYING \
	AUTHORS \
	README.md

themedir = $(datadir)/icons

install-data-hook:
	$(MKDIR_P) $(DESTDIR)/usr/share/icons
	cp -Rv rollo $(DESTDIR)/usr/share/icons/.

uninstall-hook:
	test -e $(DESTDIR)/usr/share/icons/rollo && rm -rfv $(DESTDIR)/usr/share/icons/rollo
