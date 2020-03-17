class HTML:
    def __init__(self, output=None):
        self.output = output
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self.output is not None:
            with open(self.output, "w") as fp:
                fp.write(str(self))
        else:
            print(self)

    def __str__(self):
        html = "<html>"
        if self.children:
            for child in self.children:
                html = html + "\n" + str(child)
        html += "\n</html>"
        return html

class TopLevelTag:
    def __init__(self, tag, **kwargs):
        self.tag = tag
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def __str__(self):
        html = "<%s>\n" % self.tag
        for child in self.children:
            html += str(child)
        html += "\n</%s>" % self.tag
        return html

class Tag:
    def __init__(self, tag, is_single=False, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}

        
        self.is_single = is_single
        self.children = []
        
        if klass is not None:
            self.attributes["class"] = " ".join(klass)

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass    
    

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if self.children:
            
            opening = "\n<{tag} {attrs}>".format(tag=self.tag, attrs=attrs)
            internal = "%s" % self.text
            for child in self.children:
                internal = internal + "\n" + str(child)
            ending = "</%s>" % self.tag
            return opening + internal + "\n" + ending
        else:
            if self.is_single:
                return "<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)

            else:
                if attrs:
                    return "<{tag} {attrs}>{text}</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )
                else:
                    return "<{tag}>{text}</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )

def main(output=None):
    with HTML(output=output) as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head.children.append(title)
            doc.children.append(head)
        with TopLevelTag("body") as body:
                with Tag("h1", klass=("main-text",)) as h1:
                    h1.text = "Test"
                    body.children.append(h1)
                
                with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                    with Tag("p") as paragraph:
                        paragraph.text = "another test"
                        div.children.append(paragraph)

                    with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                        div.children.append(img)

                    body.children.append(div)
                doc.children.append(body)

main() #вывод на экран
main(output="test7777.html") #запись в файл
