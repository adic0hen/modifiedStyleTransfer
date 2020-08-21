from neural_style import parse_args, render_single_image, render_video

def originalMain(commandLine):
    global args
    args = parse_args(commandLine)
    if args.video:
        render_video()
    else:
        render_single_image()


class DefaultRequest():
    def __init__(self,
        contentDir = "--content_img_dir ./image_input",
        contentData = "--content_img taj_mahal.jpg",
        contentWeight = "--content_weight 5",
        styleDir = "--style_imgs_dir ./styles",
        styleData = "--style_imgs ice.jpg shipwreck.jpg",
        styleImgsWeights = "--style_imgs_weights 0.5 0.5",
        styleweight = "--style_weight 10000",
        device = "--device /cpu:0",
        verbose = "--verbose",
        iterations = "--max_iterations 250",
        optimizer = "--optimizer adam",
        outfile = "--img_output_dir ./multipleStyles",
    ):
        self.contentDir = contentDir
        self.contentData = contentData
        self.contentWeight = contentWeight
        self.styleDir = styleDir
        self.styleData = styleData
        self.styleImgsWeights = styleImgsWeights
        self.styleweight = styleweight
        self.device = device
        self.verbose = verbose
        self.iterations = iterations
        self.optimizer = optimizer
        self.outfile = outfile

    def getRequestArgs(self):
        return [self.contentDir,
                self.contentData,
                self.contentWeight,
                self.styleDir,
                self.styleData,
                self.styleweight,
                self.styleImgsWeights,
                self.device,
                self.verbose,
                self.iterations,
                self.optimizer,
                self.outfile]


def runInternalWithArguments(requestArgs):
    commandLine = (" ".join(requestArgs)).split()
    originalMain(commandLine)

def run_modified():
    request = DefaultRequest(iterations="--max_iterations 3")
    args = request.getRequestArgs()
    runInternalWithArguments(args)



def main():
    run_modified()


if __name__ == '__main__':
    main()